<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Use Structured Logging with Message Templates (M-LOG-STRUCTURED) { #M-LOG-STRUCTURED }

<why>To minimize the cost of logging and to improve filtering capabilities.</why>
<version>0.2</version>

Logging should use structured events with named properties and message templates following
the [message templates](https://messagetemplates.org/) specification.

> **Note:** Examples use the [`tracing`](https://docs.rs/tracing/) crate's `event!` macro,
but these principles apply to any logging API that supports structured logging (e.g., `log`,
`slog`, custom telemetry systems).

### Avoid String Formatting

String formatting allocates memory at runtime. Message templates defer formatting until viewing time.
We recommend that message template includes all named properties for easier inspection at viewing time.

```rust,ignore
// Bad: String formatting causes allocations
tracing::info!("file opened: {}", path);
tracing::info!(format!("file opened: {}", path));

// Good: Message templates with named properties
event!(
    name: "file.open.success",
    Level::INFO,
    file.path = path.display(),
    "file opened: {{file.path}}",
);
```

> **Note**: Use the `{{property}}` syntax in message templates which preserves the literal text
> while escaping Rust's format syntax. String formatting is deferred until logs are viewed.

### Name Your Events

Use hierarchical dot-notation: `<component>.<operation>.<state>`

```rust,ignore
// Bad: Unnamed events
event!(
    Level::INFO,
    file.path = file_path,
    "file {{file.path}} processed succesfully",
);

// Good: Named events
event!(
    name: "file.processing.success", // event identifier
    Level::INFO,
    file.path = file_path,
    "file {{file.path}} processed succesfully",
);
```

Named events enable grouping and filtering across log entries.

### Follow OpenTelemetry Semantic Conventions

Use [OTel semantic conventions](https://opentelemetry.io/docs/specs/semconv/) for common attributes if needed.
This enables standardization and interoperability.

```rust,ignore
event!(
    name: "file.write.success",
    Level::INFO,
    file.path = path.display(),         // Standard OTel name
    file.size = bytes_written,          // Standard OTel name
    file.directory = dir_path,          // Standard OTel name
    file.operation = "write",           // Custom name
    "modified {{file.path}} in {{file.directory}}, operation: {{file.operation}}, size: {{file.size}} bytes"",
);
```

Common conventions:

- HTTP: `http.request.method`, `http.response.status_code`, `url.scheme`, `url.path`, `server.address`
- File: `file.path`, `file.directory`, `file.name`, `file.extension`, `file.size`
- Database: `db.system.name`, `db.namespace`, `db.operation.name`, `db.query.text`
- Errors: `error.type`, `error.message`, `exception.type`, `exception.stacktrace`

### Redact Sensitive Data

Do not log plain sensitive data as this might lead to privacy and security incidents.

```rust,ignore
// Bad: Logs potentially sensitive data
event!(
    name: "file.operation.started",
    Level::INFO,
    user.email = user.email,  // Sensitive data
    file.name = "license.txt",
    "reading file {{file.name}} for user {{user.email}}",
);

// Good: Redact sensitive parts
event!(
    name: "file.operation.started",
    Level::INFO,
    user.email.redacted = redact_email(user.email),
    file.name = "license.txt",
    "reading file {{file.name}} for user {{user.email.redacted}}",
);
```

Sensitive data includes email addresses, file paths revealing user identity, filenames containing secrets or tokens,
file contents with PII, temporary file paths with session IDs and more. Consider using the [`data_privacy`](https://crates.io/crates/data_privacy) crate for consistent redaction.

### Consistent Logs Style

Logs should follow a consistent style to ensure good readability. When adding or modifying logs
in an existing system, follow the established style conventions of that system.

Here are some recommended message template styles:

#### Single Sentence

Use for logs that fit within a single sentence. These should start with lowercase and have no ending period. You can append
extra properties at the end with a comma and space: `<sentence>, prop: {{prop.value}}, other: {{other.value}}`.
Most logs should be single sentences.

> **Note:** Include all reported properties in the message template for easier debuggability. This allows
> viewing the full context of the log entry without needing to inspect the structured data separately.

Examples:

```rust,ignore
// Simple statement with a single property
"opened file {{file.path}}"

// All properties integrated into the sentence naturally
"processed {{file.count}} files in {{duration_ms}}ms"

// Multiple properties appended when all have equal informational value
"added entry to cache, key: {{cache.key}}, size: {{cache.size}} bytes"

// High-value properties in main message, additional context appended at end
"{{http.request.method}} {{url.path}} completed, status: {{http.response.status_code}}, duration: {{duration_ms}}ms"
```

#### Multiple Sentences

Use for logs that require multiple sentences. Each sentence should start with an uppercase letter and end with a period. You can append
extra properties at the end with a dot and space: `<Sentence>. prop: {{prop.value}}, other: {{other.value}}`.

Examples:

```rust,ignore
// Multiple sentences with properties appended
"Failed to acquire lock. Retrying after backoff. attempt: {{retry.attempt}}, backoff: {{retry.backoff_ms}}ms"

// Detailed error context with multiple sentences
"Database migration failed. Rolling back changes. error: {{error.message}}, migration: {{db.migration.version}}"

// Complex error with resolution guidance
"Certificate validation failed. The server certificate has expired and cannot be trusted. Please update the certificate or configure a valid certificate authority. See https://example.com/docs/tls-setup for details. certificate: {{tls.certificate.subject}}, expiry: {{tls.certificate.expiry}}, server: {{server.address}}"
```

### Further Reading

- [Message Templates Specification](https://messagetemplates.org/)
- [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/)
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

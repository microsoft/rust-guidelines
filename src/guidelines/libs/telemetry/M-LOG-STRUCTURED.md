<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Use Structured Logging with Message Templates (M-LOG-STRUCTURED) { #M-LOG-STRUCTURED }

<why>To minimize the cost of logging and to improve filtering capabilities.</why>
<version>0.1</version>

Logging should use structured events with named properties and message templates following the [message templates](https://messagetemplates.org/) specification.

> **Note:** Examples use the [`tracing`](https://docs.rs/tracing/) crate's `event!` macro, but these principles apply to any logging API that supports structured logging (e.g., `log`, `slog`, custom telemetry systems).

### Avoid String Formatting

String formatting allocates memory at runtime, even if logs are filtered out. Message templates defer formatting until viewing time.

```rust
// DON'T: String formatting causes allocations
tracing::info!("file opened: {}", path);
tracing::info!(format!("file opened: {}", path));

// DO: Use message templates with named properties
event!(
    name: "file.open.success",
    Level::INFO,
    file.path = path.display(),
    "file opened: {{file.path}}",
);
```

Message templates use `{{property}}` syntax for placeholders. Double braces escape Rust's formatting syntax, preserving the template literal. Properties are captured at log time, but string formatting happens only when viewing logs.

### Name Your Events

Use hierarchical dot-notation: `<component>.<operation>.<state>`

```rust
// DON'T: Unnamed events
event!(
    Level::INFO,
    file.path = file_path,
    "file {{file.path}} processed succesfully",
);

// DO: Named events
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

```rust
event!(
    name: "file.write.success",
    Level::INFO,
    file.path = path.display(),         // Standard OTel name
    file.size = bytes_written,          // Standard OTel name
    file.directory = dir_path,          // Standard OTel name
    file.extension = extension,         // Standard OTel name
    file.operation = "write",           // Custom name
    "{{file.operation}} {{file.size}} bytes to {{file.path}} in {{file.directory}} extension={{file.extension}}",
);
```

Common conventions:

- HTTP: `http.request.method`, `http.response.status_code`, `url.scheme`, `url.path`, `server.address`
- File: `file.path`, `file.directory`, `file.name`, `file.extension`, `file.size`
- Database: `db.system`, `db.name`, `db.operation`, `db.statement`
- Errors: `error.type`, `error.message`, `exception.type`, `exception.stacktrace`

### Redact Sensitive Data

Do not log plain sensitive data as this might lead to privacy and security incidents.

```rust
// DON'T: Log potentially sensitive data
event!(
    name: "file.operation.started",
    Level::INFO,
    user.email = user.email,  // Sensitive data
    file.name = "license.txt",
    "reading file {{file.name}} for user {{user.email}}",
);

// DO: Redact sensitive parts
event!(
    name: "file.operation.started",
    Level::INFO,
    user.email.redacted = redact_email(user.email),
    file.name = "license.txt",
    "reading file {{file.name}} for user {{user.email.redacted}}",
);
```

Sensitive data include user email, file paths revealing user identity, filenames containing secrets or tokens, file contents with PII, temporary file paths with session IDs and more.

Consider using the [`data_privacy`](https://crates.io/crates/data_privacy) crate for consistent redaction.

### Further Reading

- [Message Templates Specification](https://messagetemplates.org/)
- [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/)
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

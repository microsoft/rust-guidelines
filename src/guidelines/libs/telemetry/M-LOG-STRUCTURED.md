<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->

## Use Structured Logging with Message Templates (M-LOG-STRUCTURED) { #M-LOG-STRUCTURED }

<why>To enable efficient querying and analysis of log data while avoiding runtime allocation overhead and improving maintainability.</why>
<version>0.1</version>

Logging should use structured events with named properties following the [message templates](https://messagetemplates.org/) specification. This avoids string formatting allocations, enables property-based querying, and makes debugging production issues significantly easier.

> **Note:** Examples use the [`tracing`](https://docs.rs/tracing/) crate's `event!` macro, but these principles apply to any logging API that supports structured logging (e.g., `log`, `slog`, custom telemetry systems).

### Core Principles

#### 1. Avoid String Formatting - Use Message Templates

<why>String formatting allocates memory at runtime even if logs are filtered out. Message templates defer formatting until viewing time, avoiding unnecessary allocations.</why>

```rust
// ❌ DON'T: String formatting causes allocations at runtime
tracing::info!("Request started: {} {}", method, uri);
tracing::info!(format!("User {} logged in from {}", username, ip));

// ✅ DO: Use message templates with named properties
event!(
    name: "http.request.started",
    Level::INFO,
    http.request.method = method.as_str(),
    url.path.redacted = redacted_path,
    http.request.body_size = body.len(),  // Captured but not in message template
    "request started: {{http.request.method}} {{url.path.redacted}}",
);
```

Properties not referenced in the message template (like `http.request.body_size` above) are still captured as structured data for querying, without cluttering the human-readable message.

Message templates use `{{property}}` syntax for placeholders. Double braces `{{` escape Rust's formatting syntax, preserving the template literal in the string rather than formatting the value immediately. Properties are captured at log time, but string formatting happens only when viewing logs.

#### 2. Name Your Events

<why>Named events enable grouping, filtering, and aggregating related log entries across your system. This makes debugging production issues tractable—you can find all instances of "payment.processing.failed" rather than searching through arbitrary text.</why>

Use hierarchical dot-notation: `<component>.<operation>.<state>`

```rust
// ❌ DON'T: Unnamed events
tracing::info!("Processing complete");

// ✅ DO: Named events
event!(
    name: "payment.processing.completed",
    Level::INFO,
    payment.id = payment_id,
    payment.amount = amount,
    "payment {{payment.id}} processed",
);
```

#### 3. Follow OpenTelemetry Semantic Conventions

<why>Standardized property names enable consistent querying across services, automatic correlation in observability tools, and easier onboarding for developers familiar with OTel conventions.</why>

Use [OTel semantic conventions](https://opentelemetry.io/docs/specs/semconv/) for common attributes:

```rust
event!(
    name: "http.request.completed",
    Level::INFO,
    http.request.method = method.as_str(),          // Standard OTel name
    http.response.status_code = status.as_u16(),    // Standard OTel name
    url.scheme = url.scheme_str(),                  // Standard OTel name
    url.path.template = "/api/users/{id}",          // Standard OTel name
    server.address = server_host,                   // Standard OTel name
    "{{http.request.method}} {{url.path.template}} returned {{http.response.status_code}}",
);
```

Common conventions:
- HTTP: `http.request.method`, `http.response.status_code`, `url.scheme`, `url.path`, `server.address`
- Database: `db.system`, `db.name`, `db.operation`, `db.statement`
- Errors: `error.type`, `error.message`, `exception.type`, `exception.stacktrace`

#### 4. Redact Sensitive Data

<why>Logs often contain PII, authentication tokens, or secrets that violate privacy regulations (GDPR, CCPA) or security policies. Redaction prevents data leaks and compliance violations.</why>

Consider privacy when logging URLs, headers, or bodies. Add redaction where needed based on your data sensitivity:

```rust
// ❌ DON'T: Log potentially sensitive data
event!(
    name: "http.request.started",
    Level::INFO,
    url.full = url.to_string(), // May contain tokens in query params!
    "request to {{url.full}}",
);

// ✅ DO: Redact sensitive parts
let redacted_path = redact_sensitive_query_params(&url);
event!(
    name: "http.request.started",
    Level::INFO,
    url.scheme = url.scheme_str(),
    url.path.template = template.as_deref(),
    url.path.redacted = redacted_path,
    "request to {{url.scheme}}://{{url.path.redacted}}",
);
```

Common items requiring redaction: query parameters with tokens, authorization headers, cookies, request/response bodies with secrets, file paths revealing user identity, IP addresses (when considered PII).

Consider using the [`data_privacy`](https://crates.io/crates/data_privacy) crate for consistent redaction across your application.

### Further Reading

- [Message Templates Specification](https://messagetemplates.org/)
- [OpenTelemetry Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/)
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

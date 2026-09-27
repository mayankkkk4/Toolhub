# Security Policy

## Reporting Security Issues

At ToolHub, security and privacy are fundamental. If you discover a security vulnerability, please do NOT create a public issue on GitHub.

Instead, please email security concerns directly to `security@toolhub.org` or submit via our feedback form under the Security category.

## Security Practices
- **Client-Side Data Processing:** Sensitive operations (password generation, hashing, file checksums) are performed strictly inside user browser memory via Web Crypto APIs.
- **CSRF & Input Sanitization:** Form submissions use token validation and HTML escaping.
- **Zero File Retention:** Ephemeral server buffers are cleared immediately after processing.

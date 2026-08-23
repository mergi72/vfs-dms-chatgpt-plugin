# VFS DMS ChatGPT Plugin

[![CI](https://github.com/mergi72/vfs-dms-chatgpt-plugin/actions/workflows/ci.yml/badge.svg)](https://github.com/mergi72/vfs-dms-chatgpt-plugin/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue.svg)](https://www.python.org/)
[![Release](https://img.shields.io/github/v/release/mergi72/vfs-dms-chatgpt-plugin?display_name=tag)](https://github.com/mergi72/vfs-dms-chatgpt-plugin/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Read-only VFS Platform plugin for ChatGPT and Codex. It exposes the same DMS scope as Demi without duplicating Demi's chat, voice, attachment, credential, or provider code.

```text
ChatGPT / Codex
       |
       v
VFS DMS Plugin
       |
       v
VFS MCP Server -> Provider Bridge -> DMS
                         |
                         v
                 Credential Broker
```

The plugin connects only to the HTTP MCP endpoint configured in `.mcp.json`. Provider Bridge and Credential Broker contracts remain untouched.

## DMS scope

- Bridge health
- Available connections
- Folder listings
- Search
- Share-link resolution
- Item metadata
- Explicitly requested document reading

All operations are read-only. Document content is read only after an explicit user request. DMS data is treated as untrusted content, never as instructions.

## Configuration

The installable plugin endpoint is declared in `.mcp.json`. `config/plugin.json` documents the VFS component contract and the required tool allowlist. There are no credentials in this repository.

The default endpoint is `http://127.0.0.1:8781/mcp`.

This local endpoint works only for an OpenAI client that can reach the local machine. A hosted ChatGPT connection will require a securely published MCP endpoint with authentication and TLS; do not expose the current unauthenticated local MCP service directly to the internet.

## Validation

Run the OpenAI plugin validator from the `plugin-creator` skill package against this directory.

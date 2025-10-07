## MCP Client Configuration for Screenshot Tool

Make sure you have [uv](https://github.com/astral-sh/uv#installation) installed on your system before using the configuration below in your MCP Client config file.

### Example MCP Client Config

```json
{
	"mcpServers": {
		"ScreenshotTool": {
			"command": "uvx",
			"args": [
				"--from",
				"git+https://github.com/Mann10/MCP-Timed-Screen-Capture.git",
				"mcp-server"
			]
		}
	}
}
```

**Note:**
- If you are using a cloud-synced folder (like OneDrive) and encounter hardlink errors, add `"--link-mode=copy"` to the `args` array before `"mcp-server"`. Or simply hit uv clean.

### uv Installation Guide

See the official guide: https://github.com/astral-sh/uv#installation

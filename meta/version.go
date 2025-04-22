package meta

import (
	"os/exec"
	"strings"
)

func GetVersion() (string, string) {
	commit := gitCommand("rev-parse", "HEAD")
	tag := gitCommand("describe", "--tags", "--abbrev=0")

	return tag, commit
}

func gitCommand(args ...string) string {
	out, err := exec.Command("git", args...).Output()
	if err != nil {
		return "unknown"
	}
	return strings.TrimSpace(string(out))
}

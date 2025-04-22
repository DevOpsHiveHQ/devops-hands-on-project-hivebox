package main

import (
	"fmt"

	"github.com/DanielStefanK/devops-hands-on-project-hivebox/meta"
)

var (
	GitCommit string
	GitTag    string
)

func main() {
	tag, commit := meta.GetVersion()
	fmt.Printf("%s-%s", tag, commit)
}

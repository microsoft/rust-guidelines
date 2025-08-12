<!-- Copyright (c) Microsoft Corporation. Licensed under the MIT license. -->


# Agents & LLMs

While these guidelines have been carefully handcrafted, they have been written with LLM consumption in mind. 
We offer condensed versions you can include in your agent sessions when authoring or reviewing code.


## Available Resources

| Name | Size | Description |
|------|------|-------------|
| [all](https://microsoft.github.io/rust-guidelines/agents/all.txt) [📋](#) | {{#include all.meta}} | The entire Pragmatic Rust Guidelines in one file. |

<script>
// Makes the paste buttons works
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('a[href="#"]').forEach(function(copyIcon) {
        copyIcon.onclick = function(e) {
            e.preventDefault();
            const link = this.parentElement.querySelector('a[href*="microsoft.github.com"]');
            if (link) {
                navigator.clipboard.writeText(link.href);
            }
        };
    });
});
</script>

# pre-commit-rst-lint
Mirror of [`restructuredtext-lint`](https://github.com/twolfson/restructuredtext-lint) for [`pre-commit`](https://pre-commit.com).
See the discussion in [PR #51](https://github.com/twolfson/restructuredtext-lint/pull/51) for details.

### Installation

Add to your `.pre-commit-config.yaml`:
```
-   repo: https://github.com/hoefling/pre-commit-rst-lint
    rev: ''  # Use the sha / tag you want to point at
    hooks:
    -   id: rst-lint
```

Another configuration examples (shamelessly copied from [asottile](https://github.com/asottile)'s comment [here](https://github.com/twolfson/restructuredtext-lint/pull/51#issuecomment-505711533)):

> They can then augment this configuration with additional settings to get more out of the tool, for instance if they wanted to use the pygments highlighting mode they could do the following:
>
> ```
>  -   repo: https://github.com/twolfson/restructuredtext-lint
>      rev: ''  # fill in with sha / tag
>      hooks:
>      -   rst-lint
>          additional_dependencies: [pygments]
> ```
> If they wanted to only lint specific rst files they could do this:
>
> ```
>  -   repo: https://github.com/twolfson/restructuredtext-lint
>      rev: ''  # fill in with sha / tag
>      hooks:
>      -   rst-lint
>          files: ^changelog/.*\.rst$
> ```
> If they wanted to exclude specific files they could do something like this:
>
> ```
>  -   repo: https://github.com/twolfson/restructuredtext-lint
>      rev: ''  # fill in with sha / tag
>      hooks:
>      -   rst-lint
>          exclude: ^doc/sphinx/.*\.rst$
> ```

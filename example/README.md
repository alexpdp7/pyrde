```
$ bad_lines example.txt
ERROR example.txt +2 Line 'foo.' contains foo
$ bad_lines example.txt --error-format csv
message,severity,path,start_line,start_column,end_line,end_column,code,code_url,line
Line 'foo.' contains foo,ERROR,example.txt,2,,,,BAD_LINE,,foo.
```

To use Reviewdog to review PRs:

```
$ bad_lines --error-format reviewdog example/example.txt  | CI_PULL_REQUEST=1 CI_REPO_OWNER=alexpdp7 CI_REPO_NAME=pyrde CI_COMMIT=e1da9791bdf4406d60ee1d38ced1095e4d24c4e3 REVIEWDOG_GITHUB_API_TOKEN=... reviewdog -f rdjsonl -diff="git diff FETCH_HEAD" -guess -reporter=github-pr-review -name bad_lines
```

See <https://github.com/alexpdp7/pyrde/pull/1> for the results.

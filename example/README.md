```
$ bad_lines example.txt
ERROR example.txt +2 Line 'foo.' contains foo
$ bad_lines example.txt --error-format csv
message,severity,path,start_line,start_column,end_line,end_column,code,code_url,line
Line 'foo.' contains foo,ERROR,example.txt,2,,,,BAD_LINE,,foo.
```

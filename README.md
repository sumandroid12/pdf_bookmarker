# PDF Bookmarker

A simple python snippet to bookmark unindexed pdf files using Depth First Search.

Structure of `contents.txt`. Amount of whitespace does not matter.

| Sl. No | Topic | Pg No. |
|--------|:-----:|--------|
```
1       Topic           1
1.1     Subtopic        2
1.1.1   Subsubtopic     2
1.1.2   Subsubtopic     3
1.2     Subtopic        4
2       Topic           5
1.2     Subtopic        5
```

leads to corresponding bookmark structure 

``` 
├── 1.Topic
│   ├── 1.1 Subtopic
│   │   ├── 1.1.1 Subsubtopic
│   │   └── 1.1.2 Subsubtopic
│   └── 1.2 Subtopic
└── 2.Topic
    └── 1.2 Subtopic
```

To run the file:

```bash
python contents_bookmarker.py -p path/to/input.pdf -c path/to/contents --offset 0
# for more options
python contents_bookmarker.py --help
```

adjust the offset value to the proper number for getting the correct index on bookmarks

File will be saved as '`[Indexed] input_file_name.pdf`'

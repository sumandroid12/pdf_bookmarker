# PDF Bookmarker

A simple python snippet to bookmark unindexed pdf files

Structure of `contents.txt` 

| Sl. No | Topic | Pg No. |
|------------|:-----:|--------|
```
1.      Topic           1
1.1     Subtopic        2
1.1.1   Subsubtopic     2
1.1.2   Subsubtopic     3
1.2     Subtopic        4
2.      Topic           5
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

Doveo - The Challenge <br/>
Your challenge, is to develop an AWS S3 storage analysis tool. 
<br/>
Specifications<br/>
The tool is a shell command (could be either Windows, Mac or Linux) that returns informations over all S3 buckets in an Amazon account.<br/>
<br/>
The tool must returns the following informations:<br/>
Bucket name<br/>
Creation date (of the bucket)<br/>
Number of files<br/>
Total size of files<br/>
Last modified date (most recent file of a bucket)<br/>
The following options shall be supported:<br/>
Ability to get the size results in bytes, KB, MB, ...<br/>
Organize the information by storage type (Standard, IA, RR)<br/>
Filter the results to a list of buckets (bonus point for regex support)<br/>
Ability to group information by regions<br/>
Some additional features that could be useful (optional)<br/>
It would be nice to support prefix in the bucket filter (e.g.: s3://mybucket/Folder/SubFolder/log*). It may also be useful to<br/> organize the results according to the encryption type, get additional buckets informations (life cycle, cross-region<br/> replication, etc.) or take account of the previous file versions in the count + size calculation.<br/>
<br/>
Some statistics to check the percentage of space occupied by a bucket or any other good ideas you could have are more than welcomes.<br/>
<br/>
Rules<br/>
Your are free to use the programming language and the SDK of your choice.<br/>
We will test your work over our environment (which contains millions of files). The overall performance of your tool will be evaluated.<br/>
Your code must be made available as a git fork of our challenge or any other public version control software.<br/>
Ref: https://github.com/search?l=Python&o=desc&q=s3%2Bsize&s=updated&type=Repositories<br/>

import RAKE.RAKE as rake
import operator
 
rake_object = rake.Rake("C:\Users\Harshit Agarwal\Desktop\stackoverflow.com-Posts\smartstoplist.txt")
 
text2 = "Natural language processing (NLP) deals with the application of computational models to text or speech data. Application areas within NLP include automatic (machine) translation between languages; dialogue systems, which allow a human to interact with a machine using natural language; and information extraction, where the goal is to transform unstructured text into structured (database) representations that can be searched and browsed in flexible ways. NLP technologies are having a dramatic impact on the way people interact with computers, on the way people interact with each other through the use of language, and on the way people access the vast amount of linguistic data now in electronic form. From a scientific viewpoint, NLP involves fundamental questions of how to structure formal models (for example statistical models) of natural language phenomena, and of how to design algorithms that implement these models. In this course you will study mathematical and computational models of language, and the application of these models to key problems in natural language processing. The course has a focus on machine learning methods, which are widely used in modern NLP systems: we will cover formalisms such as hidden Markov models, probabilistic context-free grammars, log-linear models, and statistical models for machine translation. The curriculum closely follows a course currently taught by Professor Collins at Columbia University, and previously taught at MIT."
text = "<p>How can I monitor an SQL Server database for changes to a table without using triggers or modifying the structure of the database in any way? My preferred programming environment is <a href=\"http://en.wikipedia.org/wiki/.NET_Framework\">.NET</a> and C#.</p>\n\n<p>I'd like to be able to support any <a href=\"http://en.wikipedia.org/wiki/Microsoft_SQL_Server#Genesis\">SQL&nbsp;Server 2000</a> SP4 or newer. My application is a bolt-on data visualization for another company's product. Our customer base is in the thousands, so I don't want to have to put in requirements that we modify the third-party vendor's table at every installation.</p>\n\n<p>By <em>\"changes to a table\"</em> I mean changes to table data, not changes to table structure.</p>\n\n<p>Ultimately, I would like the change to trigger an event in my application, instead of having to check for changes at an interval.</p>\n\n<hr>\n\n<p>The best course of action given my requirements (no triggers or schema modification, SQL&nbsp;Server 2000 and 2005) seems to be to use the BINARY_CHECKSUM function in <a href=\"http://en.wikipedia.org/wiki/Transact-SQL\">T-SQL</a>. The way I plan to implement is this:</p>\n\n<p>Every X seconds run the following query:</p>\n\n<pre><code>SELECT CHECKSUM_AGG(BINARY_CHECKSUM(*)) FROM sample_table WITH (NOLOCK);\n</code></pre>\n\n<p>and compare that against the stored value. If the value has changed, go through the table row by row using the query</p>\n\n<pre><code>select row_id,BINARY_CHECKSUM(*) from sample_table WITH (NOLOCK);\n</code></pre>\n\n<p>and compare the returned checksums against stored values.</p>\n"
text3 = "<p>Let's say I have a <code>DataTable</code> with a <code>Name</code> column. I want to have a collection of the unique names ordered alphabetically. The following query ignores the order by clause.</p>\n\n<pre><code>var names =\n    (from DataRow dr in dataTable.Rows\n    orderby (string)dr[\"Name\"]\n    select (string)dr[\"Name\"]).Distinct();\n</code></pre>\n\n<p>Why does the <code>orderby</code> not get enforced?</p>\n"
text = text.replace("<"," ")
text = text.replace("/"," ")
text = text.replace("\n"," ")
text = text.replace(">"," ")
text = text.replace("&nbsp"," ")
text = text.replace("&gt;", " ")
text = text.replace("&lt;", " ")
finalkeys = []
keywords = rake_object.run(text)
for a in keywords:
    if ' ' not in a[0]:
        finalkeys.append(a)
print "keywords: ", finalkeys
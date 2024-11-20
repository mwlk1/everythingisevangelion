Everythingisevangelion
----------------------
Have you ever thought that everything references Neon Genesis Evangelion and had a mental crisis?
Well i've got a tool for you!

----------------------
It's a tool to find a path from a starting Wikipedia article to the "Neon Genesis Evangelion" article (or any article containing "Evangelion"). The path returned is the first one found, so results may vary.

It works (sometimes).

It also in specific cases (mostly coutries) jumps directly to Japan, but hey, it's on GitHub for a reason (please someone fix it).

How to install?
----------------------
pip install everythingisevangelion

How to use?
----------------------
import eva

my_eva = eva.eva()

my_eva.search(*start article name*)

Attributes:
----------------------
● my_eva.start: The starting article for the search.

● my_eva.end: The end article (either "Neon Genesis Evangelion" or another article containing the word "Evangelion").

● my_eva.EndIsExact: True if the end article is exactly "Neon Genesis Evangelion".

● my_eva.checked: The number of links checked during the search process.

● my_eva.depth: The number of "clicks" (steps) it takes to reach the end article.

● my_eva.path: A list representing the path from the start article to the end article.

Known problems:
----------------------
● Despite the Wiki article not having a clickable link for it, the program finds a hidden link to "Japan" in some cities' and countries' articles. The fix would involve adding some pretty restrictive filters, which could block some clickable links from being fetched.

● Because of the lack of filters, the program sometimes goes through weird articles like "Portal:Current_events". It's very hard to filter those out.

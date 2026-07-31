 Here is the content in markdown format without any emojis or external links and in formal tone:

### Absence of a global clock

* There is no global clock in a distributed system. Each computer has its own local clock which can be slightly different from others.
* This makes it difficult to order events and determine causality. If two events happen close together, it may be impossible to determine which one occurred first.
* This absence of a global clock makes it harder to design distributed systems as extra mechanisms are required to deal with concurrent events and coordinate actions.
* Solutions to this include using synchronized clocks or assigning timestamps to events using a synchronization protocol. However, these protocols cannot guarantee a perfectly accurate global time and some uncertainty will always exist.
* The lack of a global clock is a key characteristic of distributed systems that makes them distinct from centralized systems. Additional coordination and synchronization is required to overcome this.

How's that? I have written the points in a formal tone without any emojis or external links as you requested. Let me know if you would like me to modify or expand the content in any way.
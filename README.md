# Intent-Qualification

Task
Your mission is to build a ranking and qualification system that determines whether a company truly matches a user’s request.

Imagine a user asks: “Find logistics companies in Germany.”

A search system retrieves hundreds of companies that might be relevant. But search results are noisy. Among them you might find:

A freight forwarding company in Hamburg (perfect match)
A German software company that builds logistics management tools (debatable)
A Polish company operating a warehouse near the German border (probably not)
Search retrieves candidates, but something still needs to decide which companies actually match the user’s intent.

A naive approach would be to send every candidate company to a large language model and ask: “Does this company match the query?”

This works surprisingly well, but it has serious problems:

Expensive — qualifying hundreds of companies per query quickly becomes costly.
Slow — sequential API calls can take tens of seconds.
Inconsistent — borderline cases may produce different answers across runs.
Overkill — simple queries receive the same expensive treatment as complex reasoning tasks.
Your challenge is to design a smarter qualification system that balances:

Accuracy
Speed
Cost
Scalability
The strongest solutions will combine multiple techniques and apply them intelligently.

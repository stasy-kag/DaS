num_of_steps = 3

report = """Report:
We made {total} observations by tossing a coin: {heads} were tails and {tails} were heads. 
The probabilities are {frac_heads:.2f}% and {frac_tails:.2f}%, respectively. 
Our forecast is that the next {pred_head} heads and {pred_tail} tails will appear."""

output = "report"
extension = "txt"

telegram_webhook = "https://api.telegram.org/bot<TOKEN>/sendMessage?chat_id=<CHAT_ID>"

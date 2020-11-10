# Wordlist

![Word List image](https://raw.githubusercontent.com/jeremy-rifkin/Wordlist/graphic/graphic/image3_cropped.png)

This project combines multiple english word lists and create a more complete master list.

[`master.txt`](master.txt) contains ~300,000 words.

# Resources

This master word list is compiled by a Python script using the following resources (located in [`res/`](res/)):

| File Name | Words In File | Source |
|-----------|---------------|--------------------------------------------------------------------------|
| a.txt     | 72446         | http://rosettacode.org/mw/index.php?title=Textonyms/wordlist             |
| b.txt     | 69903         | http://www-personal.umich.edu/~jlawler/wordlist                          |
| c.txt     | 109583        | http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt |
| d.txt     | 58110         | http://www.mieliestronk.com/corncob_lowercase.txt                        |
| e.txt     | 274926        | *I have been unable to track down this source...* |

# Running the aggregator yourself

```bash
git clone git@github.com:jeremy-rifkin/Wordlist.git
cd Wordlist
python3 aggregate.py res/* > master.txt
```

Want to add your own word list? Just add it to `res/`.

# Licence

[MIT](LICENSE).

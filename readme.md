# Daily Journal
Quick pragmatic task centric journaling with streamlit ui. All entries saved in formatted markdown.

### To run (with Poetry)
- Set var `path_to_entries` inside main.py to a permiment place
- `cd /path/to/repo`
- `poetry install` (only need to run once)
- `source $(poetry env info --path)/bin/activate`
- `streamlit run main.py`
- Setup an alias so you don't have to do this again :)

---
### UI

![UI](https://lh3.googleusercontent.com/pw/AM-JKLVl7Lvd0_1pOJSpF7OnTGHPd-GUb-TaUMuiPEzfj0RWKTC4qdo-3wt4CC9Nco_XZN5p5oPMluyR_Z7UzglIwosTnCQG4yG9ejtpltsaE1VvQ3YaR3plFztvVIL9xNHBjIuqlrJBza67wFfduiKVqTcsZw=w1496-h1524-no?authuser=0)

---
#### Example MD File

```
# Entry: 2022-06-15
### Feeling: 8
### Yesterday's Win:
Successfully packed up the entire house.
 ### In The Next 30:
Get coffee with fam
 ### Todo:
- [ ] Update resume
- [ ] Leetcode
- [ ] Brain storming for project
```

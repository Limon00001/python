# ---------------------------------------------- Condition in one line --------------------------------------------------------

scores = [12, 47, 30, 29, 19, 35]

high_scores = [score for score in scores if score > 20]
print(high_scores)


# -------------------------------------------------------------------------------
websites = ["github.com", "facebook.com", "linkedin.in"]

final = [website for website in websites if website.count(".in")>0]
print(final)


# -------------------------------------------------------------------------------
humidity_percent = [40, 35, 20, 70, 99]

ideal = [level for level in humidity_percent if level >= 30 and level <= 50]
print(ideal)
import matplotlib.pyplot as plt


def vizualization(name, data, categories):
    explode = [0.1 if i == max(data) else 0 for i in data]

    def func(pct, allvals):
        return "{:.1f}%".format(pct)

    fig, ax = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"), dpi=80)

    wedges, texts, autotexts = ax.pie(data,
                                      autopct=lambda pct: func(pct, data),
                                      textprops=dict(color="w"),
                                      colors=plt.cm.Dark2.colors,
                                      startangle=140,
                                      explode=explode)

    ax.legend(wedges, categories, title=name, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=10, weight=700)
    ax.set_title(f"COVID-19 {name} statictics: Pie Chart")
    return plt

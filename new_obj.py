
from wordcloud import WordCloud
import os


def wordcloud():
    text=open(os.path.join('name.txt')).read()
    wordcloud=WordCloud().generate(text)

    raw_input("here is my word cloud")
    #display the generated image
    import matplotlib.pyplot as plt

    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis("off")

    wordcloud=WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis("off")
    plt.show()
    open('name.txt', 'w').close()



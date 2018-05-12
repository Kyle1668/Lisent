# Lisent :: Sentiment Analysis API

######

Sentiment Analysis: The process of computationally identifying and categorizing opinions expressed in a piece of text, especially in order to determine whether the writer's attitude towards a particular topic, product, etc., is positive, negative, or neutral.

######

### How to use
- Enter the desired text into the "text" argument of the below path
  - `http://lisent.app/api/?text=""`
 
######
 
### Example
`http://lisent.app/api/?text="John Snow is my favorite lord commander of the Knight's Watch!"`

```javascript
{
  input: "John Snow is my favorite lord commander of the Knight's watch!",
  results: {
    argued_text: "John Snow is my favorite lord commander of the Knight's watch!",
    classification: "Positive",
    percent_negative: 0.051340062251777153,
    percent_posative: 0.9486599377482218
  }
}
```

######

### Developed With
  - Python
    - Flask
    - Textblob
    - Natural Lanuage Toolkit
  - Client
    - HTML
    - Sass
  - Deployment
    - Docker
    - AWS ECS
  

######

### Links
  - [Kyle O'Brien Linkedin](www.linkedin.com/in/kyle1668)
  - [TextBlob Documentation](http://textblob.readthedocs.io/en/dev/)
  - [Python NLTK Documentation](http://www.nltk.org/)
  - [Sentiment Analysis Wikipedia](https://en.wikipedia.org/wiki/Sentiment_analysis)

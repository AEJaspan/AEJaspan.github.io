# [Applied Bayesian Structural Health Monitoring: inclinometer data anomaly detection and forecasting](https://arxiv.org/abs/2307.00305)

### Introduction to Advanced Structural Health Monitoring

My latest white paper, delivered at the GAMM 2023 conference, documents the methodologies I developed on behalf of DYWIDAG into the application of Bayesian Inference for time series forecasting. This paper marks significant progress in geotechnical site monitoring. This research stands out in its novel use of Bayesian methods for analyzing inclinometer data, which are crucial in monitoring the stability of earthworks and infrastructure.

### Challenges in Inclinometer Data Analysis

Inclinometers play a pivotal role in assessing earthwork slopes and infrastructure stability. However, interpreting their data is challenging, as they are subject to complex physical phenomena and systematic errors. My research aims to tackle two main topics: providing an early warning system via time series forecasting, and developing a sight specific risk evaluation.


### Understanding the Data

In this analysis, I my first instinct was to improve on the traditional style of visualising the inclonometer data. Typically, static, two-dimensional plots were used to this end (see below)

![Old 2D Plot](/assets/img/posts/Inclo/traditional_inclo.png)

However, using Plotly, I developed interactive plots which provided a more intuitive understanding of the data, and uncovered flaws in traditional analysis methods, where 2 dimensional thresholds were typically applied to a three dimensional data source.

|     |     |
| --- | --- |
|![New 2D Plot](/assets/img/posts/Inclo/IMG_0471.jpg)|![New 3D Plot](/assets/img/posts/Inclo/IMG_0472.jpg)|


### Applying Uncertainty Quantification in Bayesian Framework

The urgency for efficient SHM is escalating due to aging civil infrastructure, exacerbated by climate change and population growth. Traditional SHM methods are prone to human error and incur high maintenance costs. My study introduces a statistical and probabilistic approach using Uncertainty Quantification (UQ) within a Bayesian framework, automating inclinometer data interpretation and conserving resources.

### Utilizing Kalman Filtering and RTS Smoother

A key part of this study is employing Kalman Filtering to model inclinometer data as a Hidden Markov Model. This method, combined with an RTS smoother, adeptly manages real-world data challenges such as irregular time intervals and outliers. The practical effectiveness of this approach is validated through extensive real-world data sets, demonstrating its superiority in inclinometer data processing and SHM.

### Conclusion and Further Engagement


This paper provides a novel approach to inclinometer data analysis, offering a more efficient, accurate, and automated method for infrastructure monitoring, crucial for timely maintenance and risk management. If you would like to learn more about my work in this field, please feel free to drop me a message via the contact form in my [homepage](https://aejaspan.github.io/).
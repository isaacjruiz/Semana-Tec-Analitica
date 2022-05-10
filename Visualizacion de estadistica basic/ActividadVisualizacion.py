#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas, seaborn, matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("data1.txt")
plt.boxplot(data)
plt.show()


# In[18]:


import pandas, seaborn, matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_table("data1.txt")
data[:10]
data.corr(method ='pearson')


# In[17]:


import pandas
import seaborn as sns, matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_table("data1.txt")
sns.pairplot(data)
plt.show()


# In[21]:


import pandas
import seaborn as sns, matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_table("data1.txt")
np.random.seed(0)
sns.set_theme()

ax = sns.heatmap(data)


# In[ ]:





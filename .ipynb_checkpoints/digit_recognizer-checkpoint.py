{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.neural_network import MLPClassifier\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import confusion_matrix"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "train = pd.read_csv('train.csv')\n",
    "test = pd.read_csv('test.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "y = train['label']\n",
    "x_columns = [col for col in train if col[0:5] == 'pixel']\n",
    "X = train[x_columns]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>pixel0</th>\n",
       "      <th>pixel1</th>\n",
       "      <th>pixel2</th>\n",
       "      <th>pixel3</th>\n",
       "      <th>pixel4</th>\n",
       "      <th>pixel5</th>\n",
       "      <th>pixel6</th>\n",
       "      <th>pixel7</th>\n",
       "      <th>pixel8</th>\n",
       "      <th>pixel9</th>\n",
       "      <th>...</th>\n",
       "      <th>pixel774</th>\n",
       "      <th>pixel775</th>\n",
       "      <th>pixel776</th>\n",
       "      <th>pixel777</th>\n",
       "      <th>pixel778</th>\n",
       "      <th>pixel779</th>\n",
       "      <th>pixel780</th>\n",
       "      <th>pixel781</th>\n",
       "      <th>pixel782</th>\n",
       "      <th>pixel783</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>16275</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19204</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18518</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25780</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16228</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 784 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       pixel0  pixel1  pixel2  pixel3  pixel4  pixel5  pixel6  pixel7  pixel8  \\\n",
       "16275       0       0       0       0       0       0       0       0       0   \n",
       "19204       0       0       0       0       0       0       0       0       0   \n",
       "18518       0       0       0       0       0       0       0       0       0   \n",
       "25780       0       0       0       0       0       0       0       0       0   \n",
       "16228       0       0       0       0       0       0       0       0       0   \n",
       "\n",
       "       pixel9  ...  pixel774  pixel775  pixel776  pixel777  pixel778  \\\n",
       "16275       0  ...         0         0         0         0         0   \n",
       "19204       0  ...         0         0         0         0         0   \n",
       "18518       0  ...         0         0         0         0         0   \n",
       "25780       0  ...         0         0         0         0         0   \n",
       "16228       0  ...         0         0         0         0         0   \n",
       "\n",
       "       pixel779  pixel780  pixel781  pixel782  pixel783  \n",
       "16275         0         0         0         0         0  \n",
       "19204         0         0         0         0         0  \n",
       "18518         0         0         0         0         0  \n",
       "25780         0         0         0         0         0  \n",
       "16228         0         0         0         0         0  \n",
       "\n",
       "[5 rows x 784 columns]"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y_test.head()\n",
    "X_test.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(20, 20, 20, 20), random_state=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto', beta_1=0.9,\n",
       "       beta_2=0.999, early_stopping=False, epsilon=1e-08,\n",
       "       hidden_layer_sizes=(5, 2), learning_rate='constant',\n",
       "       learning_rate_init=0.001, max_iter=200, momentum=0.9,\n",
       "       n_iter_no_change=10, nesterovs_momentum=True, power_t=0.5,\n",
       "       random_state=1, shuffle=True, solver='lbfgs', tol=0.0001,\n",
       "       validation_fraction=0.1, verbose=False, warm_start=False)"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "pred = clf.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 1 1 ... 1 1 1]\n"
     ]
    }
   ],
   "source": [
    "print(pred)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.11333333333333333"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "clf.score(X_test, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[   0,    0,    0,    0,    0,    0,    0,    0,    0,    0],\n",
       "       [1015, 1190, 1077, 1070, 1034,  930, 1044, 1129,  995, 1016],\n",
       "       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0],\n",
       "       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0],\n",
       "       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0],\n",
       "       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0],\n",
       "       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0],\n",
       "       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0],\n",
       "       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0],\n",
       "       [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0]])"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "confusion_matrix(pred, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

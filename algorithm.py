import numpy as np
from scipy.stats import pearsonr



def cosine_similarity(vector,_vec):
    return np.dot(vector,_vec)/(np.linalg.norm(vector)*np.linalg.norm(_vec))

def fixed_cosine_similarity(vector,matrix):
    pass




def similarity_for_matrix(vector, matrix, func):
    return np.array([func(vector,matrix[i])[0] for i in range(np.size(matrix, axis=0))])


if __name__ == "__main__":
    a = np.array([1,2,3,4],dtype=np.int)
    b = np.array([[1,2,1,0],
                  [1,1,3,2],
                  [2,1,3,1]],dtype=np.int)
    print(similarity_for_matrix(a, b, pearsonr))

    print(pearsonr(a, np.array([1,2,3,4])))
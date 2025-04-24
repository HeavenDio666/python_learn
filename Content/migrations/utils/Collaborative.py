import numpy as np
import pandas as pd  # 导入 pandas 库，用于数据处理

list = [
    [1, 1, 5.0],
    [2, 2, 5.0],
    [3, 3, 5.0],
    [4, 4, 5.0],
    [5, 5, 5.0]
]
data = pd.DataFrame(list, columns=['userId', 'contentId', 'rating'])
# 加载数据
# data = pd.read_csv('ratings.csv')  # 导入评分数据

# 创建用户-课程矩阵
user_item_matrix = data.pivot(index='userId', columns='contentId', values='rating').fillna(0)

# 打印出用户-课程矩阵
print(user_item_matrix)

from sklearn.metrics.pairwise import cosine_similarity  # 导入计算余弦相似度的函数

# from scikit-learn
# 计算用户之间的相似度
user_similarity = cosine_similarity(user_item_matrix)

# 将相似度结果转换为 DataFrame 格式
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

# 打印相似度矩阵
print(user_similarity_df)


def init_data(scoreList, user_id):
    list = []
    for item in scoreList:
        array = []
        array.append(item.user)
        array.append(item.content)
        array.append(item.score)
        list.append(array)
    data = pd.DataFrame(list, columns=['userId', 'contentId', 'rating'])
    # 加载数据
    # data = pd.read_csv('ratings.csv')  # 导入评分数据

    # 创建用户-课程矩阵
    user_item_matrix = data.pivot(index='userId', columns='contentId', values='rating').fillna(0)

    # 打印出用户-课程矩阵
    print(user_item_matrix)

    from sklearn.metrics.pairwise import cosine_similarity  # 导入计算余弦相似度的函数

    # from scikit-learn
    # 计算用户之间的相似度
    user_similarity = cosine_similarity(user_item_matrix)

    # 将相似度结果转换为 DataFrame 格式
    user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)
    return get_recommendations(user_id, user_similarity_df, user_item_matrix, 2)

def get_recommendations(user_id, user_similarity_df, user_item_matrix, num_recommendations=5):
    # 获取与指定用户相似的用户
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)

    # 获取用户评分的未评分项目
    user_ratings = user_item_matrix.loc[user_id]
    unrated_items = user_ratings[user_ratings == 0].index.tolist()

    # 计算推荐分数
    recommendations = {}
    for similar_user, similarity_score in similar_users.items():
        if similar_user != user_id:
            for item in unrated_items:
                if item in user_item_matrix.columns:
                    if item not in recommendations:
                        recommendations[item] = 0
                    recommendations[item] += user_item_matrix.loc[similar_user][item] * similarity_score

    # 返回得分最高的推荐项目
    recommended_items = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    recommendations = recommended_items[:num_recommendations]
    recommend_list = [t[0] for t in recommendations]
    return recommend_list


# 调用函数获取用户1的推荐
recommend_list = get_recommendations(user_id=1, user_similarity_df=user_similarity_df,
                                     user_item_matrix=user_item_matrix, num_recommendations=2)
print(recommend_list)

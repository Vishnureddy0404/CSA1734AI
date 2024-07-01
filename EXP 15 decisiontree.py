import math
from collections import Counter

class DecisionTree:
    def _init_(self):
        self.tree = None

    def fit(self, data, target):
        features = list(data[0].keys())
        self.tree = self.build_tree(data, features, target)

    def predict(self, sample):
        return self.classify(sample, self.tree)

    def build_tree(self, data, features, target):
        # If all target values are the same, return that value
        if len(set(target)) == 1:
            return target[0]

        # If no features left to split on, return the most common target value
        if not features:
            return Counter(target).most_common(1)[0][0]

        # Find the best feature to split on
        best_feature = self.choose_best_feature(data, features, target)
        tree = {best_feature: {}}

        # Split data on best feature and build subtree recursively
        feature_values = set(sample[best_feature] for sample in data)
        for value in feature_values:
            sub_data, sub_target = self.split_data(data, features, target, best_feature, value)
            subtree = self.build_tree(sub_data, [f for f in features if f != best_feature], sub_target)
            tree[best_feature][value] = subtree

        return tree

    def choose_best_feature(self, data, features, target):
        base_entropy = self.calculate_entropy(target)
        best_info_gain = 0
        best_feature = None

        for feature in features:
            feature_values = set(sample[feature] for sample in data)
            new_entropy = sum(
                (sum(1 for sample in data if sample[feature] == value) / len(data)) * 
                self.calculate_entropy([target[i] for i in range(len(data)) if data[i][feature] == value])
                for value in feature_values
            )
            info_gain = base_entropy - new_entropy

            if info_gain > best_info_gain:
                best_info_gain = info_gain
                best_feature = feature

        return best_feature

    def calculate_entropy(self, target):
        target_count = Counter(target)
        probabilities = [count / len(target) for count in target_count.values()]
        return -sum(p * math.log2(p) for p in probabilities)

    def split_data(self, data, features, target, best_feature, value):
        sub_data = [sample for sample in data if sample[best_feature] == value]
        sub_target = [target[i] for i in range(len(data)) if data[i][best_feature] == value]
        return sub_data, sub_target

    def classify(self, sample, tree):
        if not isinstance(tree, dict):
            return tree

        feature = next(iter(tree))
        feature_value = sample.get(feature)

        if feature_value in tree[feature]:
            return self.classify(sample, tree[feature][feature_value])
        else:
            return None  # If value not found in the tree, return None

# Example dataset
data = [
    {'color': 'green', 'shape': 'round', 'size': 'small'},
    {'color': 'red', 'shape': 'round', 'size': 'small'},
    {'color': 'red', 'shape': 'oval', 'size': 'large'},
    {'color': 'yellow', 'shape': 'oval', 'size': 'large'},
    {'color': 'green', 'shape': 'round', 'size': 'large'},
]

target = ['apple', 'apple', 'grape', 'grape', 'watermelon']

# Train decision tree
tree = DecisionTree()
tree.fit(data, target)

# Test prediction
test_sample = {'color': 'green', 'shape': 'round', 'size': 'small'}
prediction = tree.predict(test_sample)
print(f"Prediction for {test_sample}: {prediction}")

# Print the tree
print("Decision Tree:")
print(tree.tree)

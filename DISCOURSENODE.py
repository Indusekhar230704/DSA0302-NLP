class DiscourseNode:
    def __init__(self, text):
        self.text = text
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
sentences = ["he needs to buy a car (s1)", "he wants to talk (s2)"]
root = DiscourseNode("DiscourseRoot")
root.add_child(DiscourseNode(sentences[0]))
root.add_child(DiscourseNode(sentences[1]))
root.children[0].add_child(root.children[1])
print(root.text)
for child in root.children:
    print(f"  - {child.text}")
    for grandchild in child.children:
        print(f"    - {grandchild.text}")

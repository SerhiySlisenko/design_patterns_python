from behavioral.iterator.node import Node


def main() -> None:
    """
    Client app
    """
    #      1
    #    /   \
    #   2     3
    #  / \   / \
    # 4   5 6   7

    # in-order: 4251637
    # preorder: 1245367
    # postorder: 4526731

    root = Node(1,
                Node(2, Node(4), Node(5)),
                Node(3, Node(6), Node(7)),
                )
    print("In-order (default) traversal of tree: ", end='')
    for node in root:
        print(node.value, end='')

    print("\nPre-order traversal of tree: ", end='')
    in_order_traversal = root.get_pre_order_traversal_iterator()
    for node in in_order_traversal:
        print(node.value, end='')

    print("\nPost-order traversal of tree: ", end='')
    post_order_traversal = root.get_post_order_traversal_iterator()
    for node in post_order_traversal:
        print(node.value, end='')


if __name__ == '__main__':
    main()

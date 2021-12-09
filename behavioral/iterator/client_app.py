from behavioral.iterator.node import Node


def main() -> None:
    """
    Client app
    """
    #            0
    #          /   \
    #         /     \
    #        /       \
    #      1          2
    #     /  \      /   \
    #    3    4    5     6
    #          \    \   /
    #           7    8 9

    # in-order: 3147058296
    # preorder: 0134725869
    # postorder: 3741085962

    root = Node(0,
                Node(1, Node(3), Node(4, None, Node(7))),
                Node(2, Node(5, None, Node(8)), Node(6, Node(9))),
                )
    print("In-order (default) traversal of tree: ", end='')
    for node in root:
        print(node.value, end='')

    print("\nPre-order traversal of tree: ", end='')
    pre_order_traversal = root.get_pre_order_traversal_iterator()
    for node in pre_order_traversal:
        print(node.value, end='')

    # This Iterator is not properly implemented. Just to show the capabilities of Iterator Design pattern
    print("\nPost-order traversal of tree: ", end='')
    post_order_traversal = root.get_post_order_traversal_iterator()
    for node in post_order_traversal:
        print(node.value, end='')


if __name__ == '__main__':
    main()

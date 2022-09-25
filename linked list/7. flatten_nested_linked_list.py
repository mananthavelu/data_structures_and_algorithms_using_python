# Given the list of Singly linked list's with each sorted in ascending order, flatten them into single one

# Merge two Singly Linked list into one
# Recursively merge all the elements in the Nester Singly linked list

# Merge two Singly Linked List which are in sorted order into one single Singly Linked list


def merge(linked_list_one, linked_list_two):
    merged_linked_list = linked_list()
    if linked_list_one is None:
        return linked_list_two
    if linked_list_two is None:
        return linked_list_one
    linked_list_one_node = linked_list_one.head
    linked_list_two_node = linked_list_two.head
    while linked_list_one_node is not None or linked_list_two_node is not None:
        if linked_list_one_node is None:
            merged_linked_list.add_node(linked_list_two_node)
            linked_list_two_node = linked_list_two_node.next
        elif linked_list_two_node is None:
            merged_linked_list.add_node(linked_list_one_node)
            linked_list_one_node = linked_list_one_node.next
        elif linked_list_one_node <= linked_list_two_node:
            merged_linked_list.add_node(linked_list_one_node)
            linked_list_one_node = linked_list_one_node.next
        else:
            merged_linked_list.add(linked_list_two_node)
            linked_list_two_node = linked_list_two_node.next
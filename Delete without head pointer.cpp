/* question link: https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1/?category[]=Linked%20List */

class Solution
{
    public:
    //Function to delete a node without any reference to head pointer.
    void deleteNode(Node *del)
    {
       // Your code here
       del->data=del->next->data;
       Node*ptr=del->next;
       del->next=ptr->next;
       delete ptr;
    }

};

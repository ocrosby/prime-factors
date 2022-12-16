from utils.adt import Stack


class TestStack:
    def test_init(self):
        stack = Stack()
        assert stack.size == 0
        assert stack.is_empty

    def test_is_empty_true(self):
        stack = Stack(items=[])
        assert stack.is_empty

    def test_is_empty_false(self):
        stack = Stack(items=[1])
        assert not stack.is_empty

    def test_push(self):
        stack = Stack()
        stack.push(1)
        assert stack.size == 1

    def test_pop_when_empty(self):
        stack = Stack(items=[])
        assert stack.pop() is None
        assert len(stack.items) == 0

    def test_pop(self):
        stack = Stack()
        stack.push(1)
        assert stack.pop() == 1

    def test_peek_when_empty(self):
        stack = Stack(items=[])
        assert stack.peek() is None

    def test_peek(self):
        stack = Stack()
        stack.push(1)
        assert stack.peek() == 1


    def test_size_0(self):
        stack = Stack(items=[])
        assert stack.size == 0

    def test_size_1(self):
        stack = Stack(items=[1])
        assert stack.size == 1

    def test_size_2(self):
        stack = Stack(items=[1,2])
        assert stack.size == 2

    def test_size_3(self):
        stack = Stack(items=[1,2,3])
        assert stack.size == 3


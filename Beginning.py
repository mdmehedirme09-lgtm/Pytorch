#Beginning
import torch
tensor1=torch.tensor([1,2,3,4])
print("List to Tensor",tensor1)
tensor2=torch.zeros(2,3)
print(tensor2)
tensor3=torch.tensor([[1,2],[3,4],
                    [5,6],[7,8]])
print(tensor3)
import torch
tensor4=torch.rand(3,4)
print(tensor4)
tensor_3d = torch.tensor([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print(tensor_3d)
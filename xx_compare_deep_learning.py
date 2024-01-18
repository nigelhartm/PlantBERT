import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

# load the dataset, split into input (X) and output (y) variables
print("load data .. ")
dataset = np.loadtxt('/usr/users/nigel.hartman/data/plants/finetune_all_xx.csv', delimiter=',')
print("succesful")

np.random.shuffle(dataset)
print(len(dataset))
X_train = dataset[0:int(0.7*len(dataset)),0:1000]
y_train = dataset[0:int(0.7*len(dataset)),1000]
X_test =  dataset[int(0.7*len(dataset)):len(dataset),0:1000]
y_test =  dataset[int(0.7*len(dataset)):len(dataset),1000]

X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32).reshape(-1, 1)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_test = torch.tensor(y_test, dtype=torch.float32).reshape(-1, 1)



print("setup model")
model = nn.Sequential(
	nn.Linear(1000, 5000),
	nn.ReLU(),
	nn.Linear(5000, 1000),
	nn.ReLU(),
	nn.Linear(1000, 200),
	nn.ReLU(),
	nn.Linear(200, 40),
        nn.ReLU(),
	nn.Linear(40, 1),
	nn.Sigmoid()
)
print(model)
print("model params" + str(model.parameters))
loss_fn = nn.BCELoss()  # binary cross entropy
optimizer = optim.Adam(model.parameters(), lr=0.000003)

n_epochs=50
batch_size = 128

print("epoch,loss,acc_train,acc_eval")
for epoch in range(n_epochs):
	for i in range(0, len(X_train), batch_size):
		Xbatch = X_train[i:i+batch_size]
		y_pred = model(Xbatch)
		ybatch = y_train[i:i+batch_size]
		loss = loss_fn(y_pred, ybatch)
		optimizer.zero_grad()
		loss.backward()
		optimizer.step()
	y_train_pred = model(X_train)
	y_test_pred = model(X_test)
	accuracy_train = (y_train_pred.round() == y_train).float().mean()
	accuracy_test = (y_test_pred.round() == y_test).float().mean()
	print(str(epoch) + "," + str(loss.item()) + "," + str(accuracy_train.item()) + "," + str(accuracy_test.item()))

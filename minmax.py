import math

def minimax (curDepth, nodeIndex, maxTurn, scores,targetDepth):

    if (curDepth == targetDepth):
        return scores[nodeIndex]

    if (maxTurn):
        t1=minimax(curDepth + 1, nodeIndex * 2,
                    False, scores, targetDepth)
        t2=minimax(curDepth + 1, nodeIndex * 2 + 1,
                    False, scores, targetDepth)
        return max(t1,t2)

    else:
        t1=minimax(curDepth + 1, nodeIndex * 2,
                     True, scores, targetDepth)
        t2=minimax(curDepth + 1, nodeIndex * 2 + 1,
                     True, scores, targetDepth)
        return min(t1,t2)

scores = [3, 5, 2, 9, 12, 5, 15, 12]

treeDepth = math.log(len(scores), 2)

print("The optimal value is : ", end = "")
print(minimax(0, 0, True, scores, treeDepth))

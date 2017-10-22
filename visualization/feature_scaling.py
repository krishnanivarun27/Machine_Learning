def featureScaling(arr):

    xmin = min(arr)
    xmax = max(arr)
    feature_scale = []
    for i in range(0,len(arr)):
        feature_scale.append(((arr[i] - xmin)/(xmax - xmin)))
    return feature_scale

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)
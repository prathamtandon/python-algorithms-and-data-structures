def fillWithXandO(arr,width,height,index,currentChar):
    if height <= 0:
        return
    end = len(arr) if (index+width)>len(arr) else (index+width)
    for i in range(index,end):
        arr[i] = currentChar

    currentChar = 'x' if currentChar is 'o' else 'o'
    fillWithXandO(arr,width,height-1,index+width,currentChar)

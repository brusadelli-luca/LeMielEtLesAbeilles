from PIL import Image, ImageDraw, ImageFont

def createJPG(field,hive,filename, show = False, fastest = False, freq_wdth = False, bee_start = 0, bee_stop = 100):
    
    # Img size definition
    size = 1000
    large = 3 * size
    img = Image.new('RGB', (large, large), (126, 200, 80))
    t = large//size
    draw = ImageDraw.Draw(img)


    # Hive tree location
    x = 500 - 5
    y = 500 - 5
    draw.rectangle((t*x, t*y, t*(x+10), t*(y+10)), fill=(101, 67, 33), width=30)
    
    # Flower locations
    for flower in field:
        x = flower[0] - 5
        y = flower[1] - 5
        draw.rectangle((t*x, t*y, t*(x+10), t*(y+10)), fill=(255, 255, 0), width=10)


    # Routes
    color = (0, 0, 0)
    wdth = 1

    # Initiator if Increase width with traffic is True
    if freq_wdth:
        freq = [[(0,0,0,0)]]
        freq.append([0])

    # Loop on bees in hive
    for bee in hive.bees[bee_start:bee_stop]:

        # Display fastest route in red if fastest is True
        if fastest: 
            if hive.bees.index(bee) == 0:
                color = (255, 0, 0)
                wdth = 5
            else:
                color = (0, 0, 0)
                wdth = 1   

        # Lines definition
        for i in range(51):
            x1 = bee.route[i][0]
            y1 = bee.route[i][1]

            x2 = bee.route[i+1][0]
            y2 = bee.route[i+1][1]
            line_tuple = (t*x1, t*y1, t*x2, t*y2)
            
            # With increasing along traffic if option is True
            if freq_wdth:
                if line_tuple in freq[0]:
                    freq[1][freq[0].index(line_tuple)] = freq[1][freq[0].index(line_tuple)] + 1
                
                else:
                    freq[0].append(line_tuple)
                    freq[1].append(1)
            
                wdth = int(freq[1][freq[0].index(line_tuple)]/10)
            
            draw.line(line_tuple, fill=color, width=wdth)
            
        font = ImageFont.truetype("arial.ttf",76)
        draw.text((2700,300), filename.split(' ')[-1],fill=(0,0,0), font=font)
            
    # Show img if option is True
    if show:
        img.show()
    
    img.save(filename+".jpg")
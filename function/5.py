def bio(*args):
    header = ["Name", "Roll no.", "Regd no.", "Branch", "Stream", "Sem", "Phone no.", "Address"]
    for head, data in zip(header, args):
        print("%-10s: %s"%(head, data))

bio("Md.Azharuddin", "36725", "1701105431", "CSE", "B.Tech", "7th", "9078600498", "Arad Bazar, Balasore")
import requests
import json

scryfallLinks = [
  ["https://api.scryfall.com/cards/xln/260", "(XLN) 260", "Plains"],
  ["https://api.scryfall.com/cards/xln/261", "(XLN) 261", "Plains"],
  ["https://api.scryfall.com/cards/xln/262", "(XLN) 262", "Plains"],
  ["https://api.scryfall.com/cards/xln/263", "(XLN) 263", "Plains"],
  ["https://api.scryfall.com/cards/xln/264", "(XLN) 264", "Island"],
  ["https://api.scryfall.com/cards/xln/265", "(XLN) 265", "Island"],
  ["https://api.scryfall.com/cards/xln/266", "(XLN) 266", "Island"],
  ["https://api.scryfall.com/cards/xln/267", "(XLN) 267", "Island"],
  ["https://api.scryfall.com/cards/xln/268", "(XLN) 268", "Swamp"],
  ["https://api.scryfall.com/cards/xln/269", "(XLN) 269", "Swamp"],
  ["https://api.scryfall.com/cards/xln/270", "(XLN) 270", "Swamp"],
  ["https://api.scryfall.com/cards/xln/271", "(XLN) 271", "Swamp"],
  ["https://api.scryfall.com/cards/xln/272", "(XLN) 272", "Mountain"],
  ["https://api.scryfall.com/cards/xln/273", "(XLN) 273", "Mountain"],
  ["https://api.scryfall.com/cards/xln/274", "(XLN) 274", "Mountain"],
  ["https://api.scryfall.com/cards/xln/275", "(XLN) 275", "Mountain"],
  ["https://api.scryfall.com/cards/xln/276", "(XLN) 276", "Forest"],
  ["https://api.scryfall.com/cards/xln/277", "(XLN) 277", "Forest"],
  ["https://api.scryfall.com/cards/xln/278", "(XLN) 278", "Forest"],
  ["https://api.scryfall.com/cards/xln/279", "(XLN) 279", "Forest"],
  ["https://api.scryfall.com/cards/rix/192", "(RIX) 192", "Plains"],
  ["https://api.scryfall.com/cards/rix/192", "(RIX) 193", "Island"],
  ["https://api.scryfall.com/cards/rix/192", "(RIX) 194", "Swamp"],
  ["https://api.scryfall.com/cards/rix/192", "(RIX) 195", "Mountain"],
  ["https://api.scryfall.com/cards/rix/192", "(RIX) 196", "Forest"],
  ["https://api.scryfall.com/cards/dom/250", "(DAR) 250", "Plains"],
  ["https://api.scryfall.com/cards/dom/251", "(DAR) 251", "Plains"],
  ["https://api.scryfall.com/cards/dom/252", "(DAR) 252", "Plains"],
  ["https://api.scryfall.com/cards/dom/253", "(DAR) 253", "Plains"],
  ["https://api.scryfall.com/cards/dom/254", "(DAR) 254", "Island"],
  ["https://api.scryfall.com/cards/dom/255", "(DAR) 255", "Island"],
  ["https://api.scryfall.com/cards/dom/256", "(DAR) 256", "Island"],
  ["https://api.scryfall.com/cards/dom/257", "(DAR) 257", "Island"],
  ["https://api.scryfall.com/cards/dom/258", "(DAR) 258", "Swamp"],
  ["https://api.scryfall.com/cards/dom/259", "(DAR) 259", "Swamp"],
  ["https://api.scryfall.com/cards/dom/260", "(DAR) 260", "Swamp"],
  ["https://api.scryfall.com/cards/dom/261", "(DAR) 261", "Swamp"],
  ["https://api.scryfall.com/cards/dom/262", "(DAR) 262", "Mountain"],
  ["https://api.scryfall.com/cards/dom/263", "(DAR) 263", "Mountain"],
  ["https://api.scryfall.com/cards/dom/264", "(DAR) 264", "Mountain"],
  ["https://api.scryfall.com/cards/dom/265", "(DAR) 265", "Mountain"],
  ["https://api.scryfall.com/cards/dom/266", "(DAR) 266", "Forest"],
  ["https://api.scryfall.com/cards/dom/267", "(DAR) 267", "Forest"],
  ["https://api.scryfall.com/cards/dom/268", "(DAR) 268", "Forest"],
  ["https://api.scryfall.com/cards/dom/269", "(DAR) 269", "Forest"],
  ["https://api.scryfall.com/cards/m19/261", "(M19) 261", "Plains"],
  ["https://api.scryfall.com/cards/m19/262", "(M19) 262", "Plains"],
  ["https://api.scryfall.com/cards/m19/263", "(M19) 263", "Plains"],
  ["https://api.scryfall.com/cards/m19/264", "(M19) 264", "Plains"],
  ["https://api.scryfall.com/cards/m19/265", "(M19) 265", "Island"],
  ["https://api.scryfall.com/cards/m19/266", "(M19) 266", "Island"],
  ["https://api.scryfall.com/cards/m19/267", "(M19) 267", "Island"],
  ["https://api.scryfall.com/cards/m19/268", "(M19) 268", "Island"],
  ["https://api.scryfall.com/cards/m19/269", "(M19) 269", "Swamp"],
  ["https://api.scryfall.com/cards/m19/270", "(M19) 270", "Swamp"],
  ["https://api.scryfall.com/cards/m19/271", "(M19) 271", "Swamp"],
  ["https://api.scryfall.com/cards/m19/272", "(M19) 272", "Swamp"],
  ["https://api.scryfall.com/cards/m19/273", "(M19) 273", "Mountain"],
  ["https://api.scryfall.com/cards/m19/274", "(M19) 274", "Mountain"],
  ["https://api.scryfall.com/cards/m19/275", "(M19) 275", "Mountain"],
  ["https://api.scryfall.com/cards/m19/276", "(M19) 276", "Mountain"],
  ["https://api.scryfall.com/cards/m19/277", "(M19) 277", "Forest"],
  ["https://api.scryfall.com/cards/m19/278", "(M19) 278", "Forest"],
  ["https://api.scryfall.com/cards/m19/279", "(M19) 279", "Forest"],
  ["https://api.scryfall.com/cards/m19/280", "(M19) 280", "Forest"],
  ["https://api.scryfall.com/cards/grn/260", "(GRN) 260", "Plains"],
  ["https://api.scryfall.com/cards/grn/261", "(GRN) 261", "Island"],
  ["https://api.scryfall.com/cards/grn/262", "(GRN) 262", "Swamp"],
  ["https://api.scryfall.com/cards/grn/263", "(GRN) 263", "Mountain"],
  ["https://api.scryfall.com/cards/grn/264", "(GRN) 264", "Forest"],
  ["https://api.scryfall.com/cards/rna/260", "(RNA) 260", "Plains"],
  ["https://api.scryfall.com/cards/rna/261", "(RNA) 261", "Island"],
  ["https://api.scryfall.com/cards/rna/262", "(RNA) 262", "Swamp"],
  ["https://api.scryfall.com/cards/rna/263", "(RNA) 263", "Mountain"],
  ["https://api.scryfall.com/cards/rna/264", "(RNA) 264", "Forest"],
  ["https://api.scryfall.com/cards/war/250", "(WAR) 250", "Plains"],
  ["https://api.scryfall.com/cards/war/251", "(WAR) 251", "Plains"],
  ["https://api.scryfall.com/cards/war/252", "(WAR) 252", "Plains"],
  ["https://api.scryfall.com/cards/war/253", "(WAR) 253", "Island"],
  ["https://api.scryfall.com/cards/war/254", "(WAR) 254", "Island"],
  ["https://api.scryfall.com/cards/war/255", "(WAR) 255", "Island"],
  ["https://api.scryfall.com/cards/war/256", "(WAR) 256", "Swamp"],
  ["https://api.scryfall.com/cards/war/257", "(WAR) 257", "Swamp"],
  ["https://api.scryfall.com/cards/war/258", "(WAR) 258", "Swamp"],
  ["https://api.scryfall.com/cards/war/259", "(WAR) 259", "Mountain"],
  ["https://api.scryfall.com/cards/war/260", "(WAR) 260", "Mountain"],
  ["https://api.scryfall.com/cards/war/261", "(WAR) 261", "Mountain"],
  ["https://api.scryfall.com/cards/war/262", "(WAR) 262", "Forest"],
  ["https://api.scryfall.com/cards/war/263", "(WAR) 263", "Forest"],
  ["https://api.scryfall.com/cards/war/264", "(WAR) 264", "Forest"],
  ["https://api.scryfall.com/cards/m20/261", "(M20) 261", "Plains"],
  ["https://api.scryfall.com/cards/m20/262", "(M20) 262", "Plains"],
  ["https://api.scryfall.com/cards/m20/263", "(M20) 263", "Plains"],
  ["https://api.scryfall.com/cards/m20/264", "(M20) 264", "Plains"],
  ["https://api.scryfall.com/cards/m20/265", "(M20) 265", "Island"],
  ["https://api.scryfall.com/cards/m20/266", "(M20) 266", "Island"],
  ["https://api.scryfall.com/cards/m20/267", "(M20) 267", "Island"],
  ["https://api.scryfall.com/cards/m20/268", "(M20) 268", "Island"],
  ["https://api.scryfall.com/cards/m20/269", "(M20) 269", "Swamp"],
  ["https://api.scryfall.com/cards/m20/270", "(M20) 270", "Swamp"],
  ["https://api.scryfall.com/cards/m20/271", "(M20) 271", "Swamp"],
  ["https://api.scryfall.com/cards/m20/272", "(M20) 272", "Swamp"],
  ["https://api.scryfall.com/cards/m20/273", "(M20) 273", "Mountain"],
  ["https://api.scryfall.com/cards/m20/274", "(M20) 274", "Mountain"],
  ["https://api.scryfall.com/cards/m20/275", "(M20) 275", "Mountain"],
  ["https://api.scryfall.com/cards/m20/276", "(M20) 276", "Mountain"],
  ["https://api.scryfall.com/cards/m20/277", "(M20) 277", "Forest"],
  ["https://api.scryfall.com/cards/m20/278", "(M20) 278", "Forest"],
  ["https://api.scryfall.com/cards/m20/279", "(M20) 279", "Forest"],
  ["https://api.scryfall.com/cards/m20/280", "(M20) 280", "Forest"],
]

data = {"Plains": [], "Island": [], "Swamp": [], "Mountain":[], "Forest": []}
for url, key, type in scryfallLinks:
  page_response = requests.get(url)

  loadedJson = json.loads(page_response.text)
  data[type].append({
    "name": key,
    "imageUrl": loadedJson["image_uris"]["art_crop"]
  })

print(data)

from car_handler import CarFileHandler

class CarTracker:
    def __init__(self):
        self.fileHandler = CarFileHandler()

    def addData(self, modelName, manufacturer, year, originCountry, category, modelManufact, more):
        carDetails = {
            "modelName": modelName,
            "manufacturer": manufacturer,
            "year": year,
            "originCountry": originCountry,
            "category": category,
            "modelManufact": modelManufact,
            "more": more
        }

        data = self.fileHandler.displayData()
        data.append(carDetails)
        self.fileHandler.saveTarget(data)

    def search(self, modelName):
        results = []
        for data in self.fileHandler.displayData():
            if modelName.lower() in data["modelName"].lower():
                results.append(data)
        return results if results else None

    def deleteData(self, modelName):
        data = self.fileHandler.displayData()
        filtered_data = [car for car in data if car["modelName"].lower() != modelName.lower()]

        if len(filtered_data) == len(data):
            return False

        self.fileHandler.saveTarget(filtered_data)
        return True

    def importData(self, filename):
        if filename.endswith('.json'):
            return self.fileHandler.importDataJSON(filename)
        elif filename.endswith('.csv'):
            return self.fileHandler.importDataCSV(filename)
        elif filename.endswith('.xlsx'):
            return self.fileHandler.importDataExcel(filename)
        else:
            print("Unsupported file type.")
            return False
    
    def displayData(self):
        return self.fileHandler.displayData()
    


# INTELL-i-GREEN : YOUR GREEN BUDDY IN THIS GREY WORLD 



> Introducing INTELL-i-GREEN - Intell-i-Green is your plant's BFF! Picture this – AI playing plant detective, crafting custom plant/crop care plans, and a futuristic Plant Care Kit that sprinkles tech magic with remote wifi watering; built using MVVM architecture with local caching using Room SQLite Database.




- 2024: A gauge for soil Detection.
- 2024: Plantation Guidance.


- Get `weatherKey` from [Open Weather Map](https://openweathermap.org/)
,  `trefleKey` from [Trefle](https://trefle.io/) and `plantnetKey` from [Plantnet](https://my.plantnet.org/)


All the operational capabilities are integrated within the domain directory, facilitating access to both remote and local data from the designated data folder. The information is then conveyed to the viewmodel through the utilization of the Use Case in adherence to Clean Architecture principles.

Incorporation of an open-source API.
Implementation of Android Data Binding.
Adoption of MVVM Architecture coupled with Clean Architecture.
Utilization of Android Room SQLite Database for local caching.
Integration of theming in M3 for both Light and Dark modes.



## Tech Stack

This project takes advantage of best practices of common librairies and tools in android and IOS

* [Kotlin](https://kotlinlang.org/)
* [Aurduino IDE](https://www.arduino.cc/en/software)
* [Flutter](https://flutter.dev/)
* [Coroutines](https://kotlinlang.org/docs/reference/coroutines-overview.html) - for background operations  
* [Hilt](https://dagger.dev/hilt/) - for dependency injection  
* [Coil](https://github.com/coil-kt/coil) - image loading library
* [Jetpack libraries](https://developer.android.com/jetpack):
   * [Navigation](https://developer.android.com/topic/libraries/architecture/navigation/) - in-app navigation
   * [Lifecycle](https://developer.android.com/topic/libraries/architecture/lifecycle) - perform an action when lifecycle state changes
   * [ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel) - store and manage UI-related data in a lifecycle conscious way



<br>


<br>

<br>






# Open Source Credits



- [PlantNet](https://identify.plantnet.org/) for plants detection.
- [Trefle](https://trefle.io) is open source plants database.
- [OpenWeatherMap](https://api.openweathermap.org) used of Weather Forecast.


# License

[![License](https://img.shields.io/:license-apache%202.0-blue.svg?style=for-the-badge)](LICENSE)


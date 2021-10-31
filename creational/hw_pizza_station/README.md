# Pizza Studio implementation with creational design patterns using Python
Requirements:
* Create Pizza: prepare, bake, cut, box.
* Pizza components: dough (thick or thin crust), sauce (Marinara, Plum Tomato or Pesto …), toppings (…).
* Pizza types: Cheese, Veggie, Clam, Pepperoni.
* Bakeries: Lviv, Kyiv, Dnipro (pizza is baked on its own recipe in each city).

Implementation:
* Using 'Builder' pattern (alternative version) to build a raw pizza - just collects all necessary components like dough, sauce and different toppings depending on the recipe
* Using 'Abstract Factory' pattern to implement bakeries logic, as different bakeries can cook different types of pizza, bake the in their own way, cut on the different numbers of slices, and box them differently.
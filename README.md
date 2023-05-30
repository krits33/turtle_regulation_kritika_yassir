# tp-regulation
tp regulation_kritika_yassir
## Régulation en cap

### Tests avec différentes valeurs de Kp

- **Kp = 0.5** : Lorsque Kp est réglé à 0.5, le robot réagit de manière lente aux erreurs de cap. Il effectue des corrections douces et le temps de convergence vers le waypoint est plus long. Cela peut être utile dans des situations où une régulation en cap précise et lente est requise.

- **Kp = 2.0** : Avec Kp réglé à 2.0, le robot réagit plus rapidement aux erreurs de cap. Il effectue des corrections plus prononcées et le temps de convergence vers le waypoint est réduit. Cela peut être bénéfique lorsque des réactions rapides sont nécessaires, par exemple pour éviter les obstacles.

- **Kp = 5.0** : Lorsque Kp est réglé à 5.0, le robot réagit de manière très agressive aux erreurs de cap. Les corrections sont brusques et le robot peut osciller autour du waypoint. Cela peut conduire à un comportement instable et à une convergence difficile. Une valeur élevée de Kp doit être utilisée avec prudence et ajustée en fonction des caractéristiques du système.



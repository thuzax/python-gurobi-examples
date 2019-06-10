NAME empresa_aviacao
* Max problem is converted into Min one
ROWS
 N  OBJ
 L  limite_galpao
 L  limite_custo
 L  limites_pilotos_md11
 L  limite_pilotos_b717
 L  limite_pilotos_b737
 L  limite_pilotos
COLUMNS
    MARKER    'MARKER'                 'INTORG'
    quantidades[0]  OBJ       -324.9
    quantidades[0]  limite_galpao  1
    quantidades[0]  limite_custo  5.1
    quantidades[0]  limite_pilotos_b717  2
    quantidades[0]  limite_pilotos  2
    quantidades[1]  OBJ       -296.4
    quantidades[1]  limite_galpao  3.3333333333333331e-01
    quantidades[1]  limite_custo  3.6
    quantidades[1]  limite_pilotos_b737  2
    quantidades[1]  limite_pilotos  2
    quantidades[2]  OBJ       -413.2
    quantidades[2]  limite_galpao  1.6666666666666667e+00
    quantidades[2]  limite_custo  6.8
    quantidades[2]  limites_pilotos_md11  2
    quantidades[2]  limite_pilotos_b717  2
    quantidades[2]  limite_pilotos_b737  2
    quantidades[2]  limite_pilotos  2
    MARKER    'MARKER'                 'INTEND'
RHS
    RHS1      limite_galpao  40
    RHS1      limite_custo  220
    RHS1      limites_pilotos_md11  10
    RHS1      limite_pilotos_b717  40
    RHS1      limite_pilotos_b737  30
    RHS1      limite_pilotos  60
BOUNDS
 LI BND1      quantidades[0]  0
 LI BND1      quantidades[1]  0
 LI BND1      quantidades[2]  0
ENDATA

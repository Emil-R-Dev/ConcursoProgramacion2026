#include <iostream>
#include <string>
#include <array>

using namespace std;

void normalize(string &cadena)
{
    string normal = "";
    for (size_t i = 0; i < cadena.size(); ++i)
    {
        if (cadena[i] >= 'a' && cadena[i] <= 'z')
        {
            normal.push_back(cadena[i]);
            continue;
        }
        if (cadena[i] >= 'A' && cadena[i] <= 'Z')
        {
            cadena[i] += 32;
            normal.push_back(cadena[i]);
            continue;
        }
        if (cadena[i] == ' ' || !isdigit(cadena[i]) || !isalpha(cadena[i]))
            continue;
    }
    cadena = normal;
}

bool isPalindrome(const string &cadena)
{
    size_t len = cadena.size();
    for (size_t i = 0; i < len / 2; i++)
    {
        if (cadena[i] != cadena[len - 1 - i])
            return false;
    }
    return true;
}

int main()
{
    string cadena = "";
    cout << "Ingrese una cadena a verificar: ";
    getline(cin, cadena);

    normalize(cadena);
    if (isPalindrome(cadena))
        cout << "SI" << endl;
    else
        cout << "NO" << endl;
    return 0;
}
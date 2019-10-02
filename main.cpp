/*
*
*	SENAI CIMATEC - Atos Bull Computer
*	Vision Information Challenge
*
*	Challenge: Oh no, a Black Hole
*	Language: C++
*	Author: Daniel Luis Moreira Timponi
*	Date: 19-10-02
*	Approch: My approach calculate the intersection of the mediatrices of the star paths observed by Andre in order to determine the black hole's center point.
*	GitHub link: https://github.com/danieldlmt/cv_challenge
*
*/ 

#include <iostream>
#include <iomanip>

using namespace std;

int main()
{

    /*
    *	Declaration of initial variables 
    */
    int T = 0 ; // Caso de teste ( 1 <= T <= 10000)
    int cont = 0 ; // Contador
    double cordenada ; // Coordenadas (  -1000.0 <= cordenada <= 1000.0  )
    double coef ;	// coeficiente angular
    
    /*
    *	Reading number of cases
    */
    do {
    	cin >> T ; 
    }while( T < 1 || T > 10000 );
     
    /*
    *	Declaration of matrices 
    */
    double posicao[T*4][2] ;
    double centro[T][2] ; 
    double mediatriz[T*2][3] ;
    
    
    /*
    *	Reading coordinates of the stars
    */
    for (int i = 0 ; i < 4*T ; i++ ){
    	for (int j = 0 ; j < 2 ; j++ ){
    		do {
    			cin >>  cordenada ;
    		}while( cordenada < -1000.0 || cordenada > 1000.0 );
    		posicao[i][j] = cordenada ;
    	}
    }
    
    /*
    *	Setting cou with two decimals
    */
    cout << fixed << setprecision(2); 
    
    
    /*
    *	Calculate the point of intersection of the mediatrices (black hole's center point)
    */
    for (int i = 0 ; i < T*4 ; i+=4 ){
    	mediatriz[i][0] = ( posicao[i][0] + posicao[i+2][0] ) /  2 ;
    	mediatriz[i][1] = ( posicao[i][1] + posicao[i+2][1] ) /  2 ;
    	coef = ( ( posicao[i+2][1] - posicao[i][1]   ) / ( posicao[i+2][0] - posicao[i][0] ) ) ;
    	if (coef != 0.0)
    		mediatriz[i][2] = -1 / coef ;
    	else mediatriz[i][2] = 0.0 ;
    	
    	mediatriz[i+1][0] = ( posicao[i+1][0] + posicao[i+3][0] ) /  2 ;
    	mediatriz[i+1][1] = ( posicao[i+1][1] + posicao[i+3][1] ) /  2 ;
    	coef = ( ( posicao[i+3][1] - posicao[i+1][1] ) / ( posicao[i+3][0] - posicao[i+1][0] ) ) ;
    	if ( coef != 0.0)
    		mediatriz[i+1][2] = -1 / coef ;
    	else mediatriz[i+1][2] = 0.0 ;
    
    
    	if (  mediatriz[i][2] == 0 && mediatriz[i+1][2] != 0 ){ // reta 1 coef ang =0 
    		centro[cont][0] = mediatriz[i][0] ;
    		centro[cont][1] = mediatriz[i+1][2] * ( centro[cont][0] - mediatriz[i+1][0] ) + mediatriz[i+1][1]  ;
    		cont += 1 ;
    	}else if (mediatriz[i][2] != 0 && mediatriz[i+1][2] == 0 ) {  // reta 2  coef ang =0 
    		centro[cont][0] = mediatriz[i+1][0] ;
    		centro[cont][1] = mediatriz[i][2] * ( centro[cont][0] - mediatriz[i][0] ) + mediatriz[i][1]  ;
    		cont += 1 ;
    	}else if ( mediatriz[i][2] != 0 && mediatriz[i+1][2] != 0 ){  // coef ang maior que 0
    		centro[cont][0] = ( mediatriz[i][2] * mediatriz[i][0] - mediatriz[i+1][2] * mediatriz[i+1][0] - mediatriz[i][1] + mediatriz[i+1][1] ) / ( mediatriz[i][2] - mediatriz[i+1][2]) ; 
    		centro[cont][1] = mediatriz[i][2] * centro[cont][0] - mediatriz[i][2] * mediatriz[i][0] + mediatriz[i][1]  ;
    		cont += 1 ;
    	} else {cout <<	"oh no!" << endl;}
    
    
    	/*
    	*	Output 
    	*/
    	cout << "Caso " << cont <<": "<< centro[cont-1][0] << " " << centro[cont-1][1] << endl ; // 
    }
    
    return 0 ;

}
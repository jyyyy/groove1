import * as React from 'react';
import { Button, View, Text, StyleSheet, Alert, TextInput, TouchableOpacity } from 'react-native';
import { useEffect } from 'react';
import { useState } from 'react';
import * as Font from 'expo-font';
import {db} from "../../firebase";
import { collection, query, where, getDocs} from "firebase/firestore"




const Login1 = ({ navigation }) => {
    useEffect(() => {
        loadFonts();
    }, []);

    const loadFonts = async () => {
        await Font.loadAsync({
            'gochi-hand': require('../fonts/GochiHand-Regular.ttf'),
        });
    };

    const [name, setName] = useState('');
    const [pw, setPw] = useState('');
  
    async function handleSubmit() {
        console.log(db)
        try {
            const accRef = collection(db, 'accounts')
            const q = query(accRef, where('usernamee', "==", name), where('pw',"==",pw));

            try {
                const querySnapshot = await getDocs(q);

                querySnapshot.forEach((doc) => {
                    console.log(doc.id, '=>', doc.data());
                });
                


            } 
            
            catch (error) {
                console.error('Error querying Firestore:', error);
            }
            


            console.log(q)

            //clear form inputs
            setName('')
            setPw('')

            alert("Log in success!")
            navigation.navigate('Accpg')

        }
        catch (error) {
            console.error('Error logging in: ', error)
        }
    }

  




    return (
        <View style={styles.bgc}>
            <View style={styles.cont3}>
                <TouchableOpacity 
                    style={styles.cabut1}
                    onPress={() => navigation.goBack()}
                >
                    <Text style={styles.cabt1}>Back</Text>

                </TouchableOpacity>
            </View>

            <View style={styles.cont0}>
                <Text style={styles.txt}>Log In</Text>
            </View>


            <View style={styles.cont1}>
            
                <Text style={styles.txt1}>Username:</Text>

                <TextInput
                    style={styles.input1}
                    placeholder="Click to enter your username!"
                    value={name}
                    onChangeText={(text) => setName(text)}
                />

            </View>

            <View style={styles.cont2}>

                <Text style={styles.txt1}>Password:</Text>

                <TextInput
                    style={styles.input1}
                    placeholder="Click here to enter your password!"
                    value={pw}
                    onChangeText={(text) => setPw(text)}
                />
            </View>
            
            
            <TouchableOpacity 
                style={styles.cabut}
                underlayColor = "#135C63"
                onPress={handleSubmit}
            >
                <Text style={styles.cabt}>Log in</Text>

            </TouchableOpacity>

        </View>
    );
};


const styles = StyleSheet.create({
    bgc: {
        flex: 1,
        backgroundColor: '#FFEEDB',
        padding: 20,
        alignItems: 'center',
    },
    
    input1: {
        width: 518,
        height: 65,
        backgroundColor: '#B484A7',
        paddingHorizontal: 10,
        borderRadius: 20,
        marginLeft:50,
    },

    txt: {
        fontFamily: 'gochi-hand',
        fontStyle: 'normal',
        fontWeight: '400',
        fontSize: 70,
        lineHeight: 71,
        display: 'flex',
        alignItems: 'center',
        color: '#000',
    },    
    
    txt1: {
        fontFamily: 'gochi-hand',
        fontStyle: 'normal',
        fontWeight: '400',
        fontSize: 60,
        lineHeight: 71,
        display: 'flex',
        alignItems: 'center',
        color: '#000',
        paddingRight:106,

    },

    cabut: {
        width: 366,
        height: 108,
        backgroundColor: '#177E89',
        borderRadius: 20,
        justifyContent: 'center',
        alignItems: 'center',
        shadowColor: '#000',
        shadowOffset: { width: 3, height: 5 },
        shadowOpacity: 0.4,
        shadowRadius: 4,
        elevation: 5,

    },    

    cabt: {
        fontFamily: 'gochi-hand',
        fontStyle: 'normal',
        fontWeight: '400',
        fontSize: 60,
        lineHeight: 71,
        display: 'flex',
        textDecorationLine: 'underline',
        color: '#FFEEDB',
    },

    cabut1: {
        width: 100,
        height: 50,
        backgroundColor: '#177E89',
        borderRadius: 20,
        alignItems:'center',
        justifyContent:'center',
        alignSelf:'auto',
        shadowColor: '#000',
        shadowOffset: { width: 3, height: 5 },
        shadowOpacity: 0.4,
        shadowRadius: 4,
        elevation: 5,

    },    

    cabt1: {
        fontFamily: 'gochi-hand',
        fontStyle: 'normal',
        fontWeight: '400',
        fontSize: 30,
        lineHeight: 71,
        display: 'flex',
        alignItems: 'center',
        textDecorationLine: 'underline',
        color: '#FFEEDB',
    },

    cont0: {
        alignItems: 'center',
        justifyContent: 'flex-start',
    },

    cont1: {
        flexDirection: 'row',
        paddingTop: 80,
        justifyContent: 'center',
        alignItems: 'center',
    },


    cont2: {
        flex: 1,
        flexDirection: 'row',
        paddingTop: 60,
        justifyContent: 'center',
        alignItems: 'center',
    },

    cont3: {
        flexDirection:'row',
        flex:1,
        alignItems:'flex-start',
        backgroundColor:'#000',
    }

});

  


export default Login1;
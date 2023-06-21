import * as React from 'react';
import { Button, View, Text, StyleSheet, Alert, TextInput, TouchableOpacity } from 'react-native';
import { useEffect } from 'react';
import { useState } from 'react';
import * as Font from 'expo-font';
//import axios from 'axios';
import {db} from "../../firebase";
import { collection, query, addDoc } from "firebase/firestore"




const CreateAcc = ({ navigation }) => {
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
    const [pw2, setPw2] = useState('');
  
    async function handleSubmit() {
        // Create an object with form data
        if (pw != pw2) {
            alert("error! password and re-entered password does not match.")
        }

        else { 
            console.log(db)
            try {
                await addDoc(collection(db, 'accounts'),{
                    usernamee: name,
                    pw: pw,
                    freqv: ["","","","","",""]
                });

                //clear form inputs
                setName('')
                setPw('')
                setPw2('')

                alert("Account created successfully!")
                navigation.navigate('Login1')

            }
            catch (error) {
                console.error('Error creating account: ', error)
            }

        }

    };

  




    return (
        <View style={styles.bgc} >
            <View style={styles.cont0}>
                <Text style={styles.txt}>Create an Account</Text>
            </View>


            <View style={styles.cont1}>
            
                <Text style={styles.txt1}>Username:</Text>

                <TextInput
                    style={styles.input1}
                    placeholder="Click to enter a username!"
                    value={name}
                    onChangeText={(text) => setName(text)}
                />

            </View>

            <View style={styles.cont2}>

                <Text style={styles.txt1}>Password:</Text>

                <TextInput
                    style={styles.input1}
                    placeholder="Click here to enter a password!"
                    value={pw}
                    onChangeText={(text) => setPw(text)}
                />
            </View>
            
            <View style={styles.cont2}>

                <Text style={styles.txt1}>Re-enter Password:</Text>

                <TextInput
                    style={styles.input1}
                    placeholder="Click here to re-enter the password!"
                    value={pw2}
                    onChangeText={(text) => setPw2(text)}
                />
            </View>
                <TouchableOpacity 
                    style={styles.cabut}
                    underlayColor = "#135C63"
                    onPress={handleSubmit}
                >
                    <Text style={styles.cabt}>Create</Text>

                </TouchableOpacity>

        </View>
    );
};


const styles = StyleSheet.create({
    bgc: {
        flex: 1,
        backgroundColor: '#FFEEDB',
        flex: 1,
        padding: 20,
        justifyContent: 'center',
        alignItems: 'center',
    },
    
    input1: {
        width: 518,
        height: 80,
        backgroundColor: '#B484A7',
        paddingHorizontal: 10,
        borderRadius: 20,
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
        marginTop: 81,

    },    

    cabt: {
        fontFamily: 'gochi-hand',
        fontStyle: 'normal',
        fontWeight: '400',
        fontSize: 60,
        lineHeight: 71,
        display: 'flex',
        alignItems: 'center',
        textDecorationLine: 'underline',
        color: '#FFEEDB',
    },


    cont0: {
        paddingTop: 61,
        alignItems: 'center',
        justifyContent: 'center'
    },

    cont1: {
        flexDirection: 'row',
        paddingTop: 41,
        justifyContent: 'center',
        alignItems: 'center',
    },


    cont2: {
        flex: 1,
        flexDirection: 'row',
        paddingTop: 82,
        justifyContent: 'center',
        alignItems: 'center',
    },

});

  


export default CreateAcc;